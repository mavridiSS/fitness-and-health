class WorkoutForm
  include ActiveModel::Conversion
  include ActiveModel::Validations
  include ActiveModel::Naming

  attr :workouts_count, :difficulty

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
end
