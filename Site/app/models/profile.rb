class Profile < ActiveRecord::Base
  belongs_to :user
  validates :nickname, presence: true
  validates :gender, presence: true
  validates :weight, allow_nil: true, numericality: { greater_then: 30, less_then: 300}
  validates :height, allow_nil: true, numericality: { greater_then: 1.00 , less_then: 2.50 }
end
