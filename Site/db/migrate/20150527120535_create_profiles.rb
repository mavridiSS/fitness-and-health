class CreateProfiles < ActiveRecord::Migration
  def change
    create_table :profiles do |t|
      t.string :nickname, index: true, null: false, unique: true
      t.string :gender, index: true, null: false
      t.float :height, index: true
      t.float :weight, index: true
      t.belongs_to :user

      t.timestamps null: false
    end
  end
end
