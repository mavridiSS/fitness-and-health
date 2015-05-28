class User < ActiveRecord::Base
  has_secure_password
  has_one :profile
  validates_uniqueness_of :email
  validates :email, presence: true
  validates :password, presence: true, confirmation: true
  validates :password_confirmation, presence: { on: [:create]}
end