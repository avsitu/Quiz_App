require "json"

file = File.read("arithmetic.json")
hash = JSON.parse(file)

p = hash["problems"]

i = 0
p.each do |k, v|
	if i == 3
		break
	end
	puts k['question']
	i += 1
end