class CreateSubCategories < ActiveRecord::Migration
  def change
    create_table :sub_categories do |t|
      t.string :subject
      t.integer :cat_id

      t.timestamps null: false
    end
  end
end
