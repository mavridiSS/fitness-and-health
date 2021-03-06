# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20150529131941) do

  create_table "profiles", force: :cascade do |t|
    t.string   "nickname",   null: false
    t.string   "gender",     null: false
    t.float    "height"
    t.float    "weight"
    t.integer  "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string   "first_name"
    t.string   "last_name"
  end

  add_index "profiles", ["gender"], name: "index_profiles_on_gender"
  add_index "profiles", ["height"], name: "index_profiles_on_height"
  add_index "profiles", ["nickname"], name: "index_profiles_on_nickname"
  add_index "profiles", ["weight"], name: "index_profiles_on_weight"

  create_table "users", force: :cascade do |t|
    t.string   "email",           null: false
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
    t.string   "password_digest"
  end

  add_index "users", ["email"], name: "index_users_on_email", unique: true
  add_index "users", ["password_digest"], name: "index_users_on_password_digest"

  create_table "workout_programs", force: :cascade do |t|
    t.text    "json_serialized_data", null: false
    t.integer "user_id"
  end

  add_index "workout_programs", ["json_serialized_data"], name: "index_workout_programs_on_json_serialized_data"

end
