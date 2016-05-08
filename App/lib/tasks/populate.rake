require 'json'

def get_category(problem)
	hashes = []
	temp = {}
	problem.each do |k, v|
		temp["name"] = k["category_id"]
		hashes << temp
	end
	Category.create(hashes)
end

namespace :populate do

	desc 'import category from arithmetic'
	task :import_category => :environment do
		file = File.read("arithmetic.json")
		hash = JSON.parse(file)

		p = hash["problems"]
		get_category(p)
	end
end #namespace