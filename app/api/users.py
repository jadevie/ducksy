from flask import Blueprint, request
from flask_login import login_required, current_user, login_user
from sqlalchemy.exc import IntegrityError
from app.forms import SignupForm, validation_errors_formatter
from app.models import db, User


bp = Blueprint("users", __name__, url_prefix="/users")


# def validation_errors_formatter(validation_errors):
#     """
#     Simple function that turns the WTForms validation errors into a simple list
#     """
#     errorMessages = []
#     for field in validation_errors:
#         for error in validation_errors[field]:
#             errorMessages.append(f'{field} : {error}')
#     return errorMessages


@bp.route("",  methods=["POST"])
def signup():
    if current_user.is_authenticated:
        return 'User has logged in'
    form = SignupForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        if User.query.filter(User.email == data['email']).one_or_none():
            return {'errors': {'email': "Email has been registered."}}, 401
        user = User(
            display_name=data['display_name'],
            email=data['email'],
            password=data['password'],
            profile_picture_url=data['profile_picture_url']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_formatter(form.errors)}, 401


@bp.route("/<user_id>",  methods=["PUT"])
@login_required
def update_user(user_id):
    if int(user_id) != current_user.id:
        return {'errors': ['Unauthorized']}, 401
    form = SignupForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        user = User.query.get(current_user.id)
        user.update(
            display_name=data['display_name'],
            email=data['email'],
            password=data['password'],
            profile_picture_url=data['profile_picture_url']
        )
        db.session.commit()
        return user.to_dict()
    return {'errors': validation_errors_formatter(form.errors)}, 401
