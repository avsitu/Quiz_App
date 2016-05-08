require 'json'

def get_category(p)
	hashes = []
	test = []
	temp = {}
	p.each do |k, v|
		name = k["category_id"]
		if (!test.include?(name))		#doesn't include
			test << name
			temp["name"] = name
			hashes << temp
		end
	end
	Category.create(hashes)
end

def get_sub(p)
	hashes = []
	test = []
	temp = {}
	p.each do |k, v|
		cat = k["category_id"]
		c = Category.find_or_create_by(:name => cat)
		sub = k["sub_cat_id"]
		if (!test.include?(sub))		#doesn't include
			test << sub
			temp["subject"] = sub
			temp["cat_id"] = c.id
			hashes << temp
		end
	end
	SubCategory.create(hashes)
end

def get_topic(p)
	hashes = []
	test = []
	temp = {}
	p.each do |k, v|
		sc = k["sub_cat_id"]
		s = SubCategory.find_or_create_by(:subject => sc)
		tn = k["topic_id"]
		if (!test.include?(tn))		#doesn't include
			test << tn
			temp["topic_n"] = tn
			temp["sc_id"] = s.id
			hashes << temp
		end
	end
	Topic.create(hashes)
end

def get_question(p)
	hashes = []
	temp = {}
	p.each do |k, v|
		temp["ask"] = k["question"]
		temp["correct_answer"] = k["answer"]
		temp["correct"] = false
		s = SubCategory.find_or_create_by(:subject => k["sub_cat_id"])
		temp["sub_cat_id"] = s.id
		c = Category.find_or_create_by(:name => k["category_id"])
		temp["category_id"] = c.id
		hashes << temp
	end
	Question.create(hashes)
end

namespace :populate do

	desc 'import category from arithmetic'
	task :import_category => :environment do
		file = File.read("arithmetic.json")
		hash = JSON.parse(file)

		p = hash["problems"]
		get_category(p)
	end

	desc 'import sub_category from arithmetic'
	task :import_sub_category => :environment do
		file = File.read("arithmetic.json")
		hash = JSON.parse(file)

		p = hash["problems"]
		get_sub(p)
	end

	desc 'import topic from arithmetic'
	task :import_topic => :environment do
		file = File.read("arithmetic.json")
		hash = JSON.parse(file)

		p = hash["problems"]
		get_topic(p)
	end

	desc 'import question from arithmetic'
	task :import_question => :environment do
		file = File.read("arithmetic.json")
		hash = JSON.parse(file)

		p = hash["problems"]
		get_question(p)
	end
end #namespace