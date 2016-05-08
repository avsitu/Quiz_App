class ChangeAnswerToAsk < ActiveRecord::Migration
  def change
	rename_column :questions, :answer, :ask
  end
end
