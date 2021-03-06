class WorkoutProgram < ActiveRecord::Base
  belongs_to :user
  class << self
    def new_json(data = test_wp_json)
      data = data.serialize
      WorkoutProgram.new(data)
    end
  end
  private

  def test_wp_json
    wp = { 
           day1: { w1: 'name1', w2: 'name2', w3: 'name3' },
           day2: { w1: 'name4', w2: 'name3', w3: 'name5' },
           day3: { w1: 'name6', w2: 'name6', w3: 'name8'}
          }

    wp.toJson
  end

  
end