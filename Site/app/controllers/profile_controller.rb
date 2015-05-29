class ProfileController < ApplicationController
  def show
    @profile = User.find(session[:user_id]).profile
  end

  def edit
    @profile = User.find()
  end

  def update
    
  end
end