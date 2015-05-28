class UsersController < ApplicationController
  
  # GET /users/new
  def registration
    @user = User.new
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

  def sign_in
    @login = Login.new
  end

  def checkout
    @login = Login.new(login_params)
    if @login.create
      session[:user_id] = @login.user.id
      cookies.permanent[:user_id] = @login.user.id if @login.memorable
      redirect_to root_path
    else
      render :sign_in
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_user
      @user = User.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def user_params
      params.require(:user).permit(:email, :password, :password_confirmation)
    end

    def login_params
      params.require(:login).permit(:email, :password, :memorable)
    end

end
