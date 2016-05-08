class CreateTopics < ActiveRecord::Migration
  def change
    create_table :topics do |t|
      t.integer :sc_id
      t.string :topic_n

      t.timestamps null: false
    end
  end
end
