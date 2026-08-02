# Checks every _people/*.md file's front matter actually parsed and has
# non-empty name/section/role — Jekyll swallows a front-matter parse error
# per-document instead of failing the whole build, so `jekyll build` can
# succeed while a person's page silently renders with every field blank.
require "yaml"
require "date"

REQUIRED = %w[name section role].freeze
VALID_SECTIONS = %w[pi postdoc pgr visitor old_friends].freeze

errors = []

Dir.glob("_people/*.md").sort.each do |file|
  content = File.read(file)
  match = content.match(/\A---\n(.*?\n)---\n/m)

  if match.nil?
    errors << "#{file}: no front matter block found"
    next
  end

  begin
    front_matter = YAML.safe_load(match[1], permitted_classes: [Date, Time])
  rescue StandardError => e
    errors << "#{file}: front matter failed to parse (#{e.message})"
    next
  end

  unless front_matter.is_a?(Hash)
    errors << "#{file}: front matter did not parse to a mapping"
    next
  end

  REQUIRED.each do |key|
    value = front_matter[key]
    errors << "#{file}: #{key} is missing or empty" if value.nil? || value.to_s.strip.empty?
  end

  section = front_matter["section"]
  if section && !VALID_SECTIONS.include?(section)
    errors << "#{file}: section #{section.inspect} is not one of #{VALID_SECTIONS.join(' / ')}"
  end
end

if errors.empty?
  puts "All _people/*.md files have valid name/section/role."
else
  puts "The following _people/*.md files have problems:"
  errors.each { |e| puts "  - #{e}" }
  exit 1
end
