class CreateWorkoutPrograms < ActiveRecord::Migration
  def change
    create_table :workout_programs do |t|
      t.text :json_serialized_data , index: true, null: false
    end
  end
end
