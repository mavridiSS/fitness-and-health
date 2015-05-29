class Add < ActiveRecord::Migration
  def change
    add_column :workout_programs, :user_id, :integer
  end
end
