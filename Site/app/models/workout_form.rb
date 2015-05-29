class WorkoutForm
  include ActiveModel::Conversion
  include ActiveModel::Validations
  include ActiveModel::Naming

  attr_accessor :workouts_count, :difficulty

   def initialize(attributes = {})
    self.attributes = attributes
  end

  def attributes=(attributes)
    attributes.each do |key, value|
      send "#{key}=", value
    end
  end

  def persisted?
    false
  end

  def json_settings
    {'difficulty' => self.difficulty, 'workouts_count' => self.workouts_count}.to_json
  end
end
