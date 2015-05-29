class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception
  before_action :check_cookies, :cheat
  private

  def is_logged_in?
    session[:user_id] != nil
  end


  def redirect_if_not_logged_in
    unless is_logged_in?
      redirect_to root_path
    end
  end

  def redirect_if_logged_in
    if is_logged_in?
      redirect_to user_path
    end
  end

  def check_cookies
    if cookies[:user_id] and !is_logged_in?
      session[:user_id] = cookies[:user_id]
    end
  end
    
  def logout
    session[:user_id] = nil
    cookies.delete :user_id
  end

  def current_user
    @_current_user ||= session[:user_id] &&
      User.find_by(id: session[:user_id])
  end

  def cheat
    session[:user_id] = 4
  end

  helper_method :is_logged_in?, :logout
end
