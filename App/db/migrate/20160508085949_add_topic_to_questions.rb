class AddTopicToQuestions < ActiveRecord::Migration
  def change
	add_column :questions, :topic, :string
  end
end
