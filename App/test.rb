require "json"

file = File.read("science.json")
hash = JSON.parse(file)

hash.each do |k, v|
	puts k
	puts " "
end
