class WorkoutProgramsController < ApplicationController

  def index
  end

  def new
    @workout_form = WorkoutForm.new
  end

end
