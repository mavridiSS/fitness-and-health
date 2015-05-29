class User < ActiveRecord::Base
  has_secure_password
  before_create :create_person
  has_one :profile
  has_one :login
  has_many :workout_programs
  validates_uniqueness_of :email
  validates :email, presence: true
  validates :password, presence: true, confirmation: true
  validates :password_confirmation, presence: { on: [:create]}

  private

  def create_person
    self.profile = Profile.new(nickname: get_nickname, gender: 'male')
  end


  def get_nickname
    email = self.email
    nickname = /.*@/.match(email).to_s[0..-2]
  end
end
