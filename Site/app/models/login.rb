class Login
  include ActiveModel::Conversion
  include ActiveModel::Validations
  include ActiveModel::Naming

  attr_accessor :email, :password, :memorable

  validates :email, :password, presence: { message: 'Неможе да има празно поле' }

  validate :email_exists_and_password_correctness


  def initialize(attributes = {})
    self.attributes = attributes
  end

  def attributes=(attributes)
    attributes.each do |key, value|
      send "#{key}=", value
    end
  end

  def create
    return false unless valid?
    true
  end


  def user
    User.find_by(email: email)
  end

  private
  MAIN_ERROR_MESSAGE = "Имейла и паролата не съвпадат."

  def email_exists_and_password_correctness
    if email_does_not_exists? or password_uncorrect?
      errors[:base] << MAIN_ERROR_MESSAGE
    end
  end

  def email_does_not_exists?
    user.nil?
  end

  def password_uncorrect?
    !user.authenticate(password)
  end

end