class AddSubCategoryToQuestions < ActiveRecord::Migration
  def change
	add_column :questions, :sub_category, :string
  end
end
