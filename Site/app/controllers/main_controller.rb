class MainController < ApplicationController
  def index
    @login = Login.new
    render :index, :layout => 'main'
  end

  def checkout
    @login = Login.new(login_params)
    if @login.create
      session[:user_id] = @login.user.id
      cookies.permanent[:user_id] = @login.user.id if @login.memorable
      redirect_to root_path
    else
      render :index
    end
  end

  private

  def send_request
    a = HttpHandlerer.new
    post_result = a.send_setting(1, {a: 'stoil e gei', b: 'mavridis e gei'})
    result = a.get_with_id(1)
  end


    def login_params
      params.require(:login).permit(:email, :password, :memorable)
    end
  helper_method :send_request
end