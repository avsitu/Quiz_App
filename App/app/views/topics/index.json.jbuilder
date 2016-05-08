json.array!(@topics) do |topic|
  json.extract! topic, :id, :id, :sc_id, :topic_n
  json.url topic_url(topic, format: :json)
end
