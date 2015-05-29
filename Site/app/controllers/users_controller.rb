class UsersController < ApplicationController

  # GET /users/new
  def registration
    @user = User.new
    render :registration, layout: 'main'
  end
  # POST /users
  # POST /users.json
  def create
    @user = User.new(user_params)

    if @user.save
      redirect_to root_path, notice: 'User was successfully created.'
    else
      render :registration
    end
  end


  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_params
      params.permit(:email, :password, :password_confirmation)
    end

end
