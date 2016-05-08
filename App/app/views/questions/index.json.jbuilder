json.array!(@questions) do |question|
  json.extract! question, :id, :id, :answer, :a, :b, :c, :d, :correct_answer, :correct, :category_id, :sub_cat_id
  json.url question_url(question, format: :json)
end
