class CreateQuestions < ActiveRecord::Migration
  def change
    create_table :questions do |t|
      t.text :answer
      t.text :a
      t.text :b
      t.text :c
      t.text :d
      t.text :correct_answer
      t.boolean :correct
      t.integer :category_id
      t.integer :sub_cat_id

      t.timestamps null: false
    end
  end
end
