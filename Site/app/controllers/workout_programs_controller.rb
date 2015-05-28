class WorkoutProgramsController < ApplicationController

  def index
    @workout_programs = [ 
                          {1: 'лежанка нормален хват', 2: 'кофички'}
                          {1: 'Лежанка тесен хват', 2: 'трицепсово сгъване с дъмбел'}
                          {1: 'Лежанка тесен хват', 2: 'трицепсово сгъване с дъмбел'}
                        ]
  end

  def show
    
  end
end