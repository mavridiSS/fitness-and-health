class ChangePasswordInUsers < ActiveRecord::Migration
  def change
    remove_column :users, :password, :string, null: false
    add_column :users, :password_digest, :string
    add_index :users, :password_digest
  end
end
