require "json"

file = File.read("arithmetic.json")
hash = JSON.parse(file)

p = hash["problems"]

temp = []
i = 0
p.each do |k, v|
	name = k['topic_id']
	if(!temp.include?(name))
		temp << name
	end
end

puts temp