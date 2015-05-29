class WorkoutProgramsController < ApplicationController

  def index
    user = current_user
    @programs = user.workout_programs
  end

  def new
    @workout_form = WorkoutForm.new
  end

  def create
    @workout_form = WorkoutForm.new(workouts_count: params["workouts_count"], difficulty: params[:workout_form]['difficulty'])
    user = current_user
    data = @workout_form.json_settings
    new_program = HttpHandlerer.new.get_program(user.id, data)
    @workout_program = WorkoutProgram.new(json_serialized_data: new_program)
    user.workout_programs << @workout_program
    redirect_to workout_programs_path
  end

end
