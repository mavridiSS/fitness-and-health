class WorkoutProgramsController < ApplicationController

  def index
  end

  def new
    @workout_program = WorkoutProgram.new
  end

end