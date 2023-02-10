from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateFeedbackForm
import shelve, Feedback
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/thankYou')
def thank_you():
    return render_template('thankYou.html')

@app.route('/createFeedback', methods=['GET', 'POST'])
def create_feedback():
    create_feedback_form = CreateFeedbackForm(request.form)
    if request.method == 'POST' and create_feedback_form.validate():
        feedbacks_dict = {}
        db = shelve.open('feedback.db', 'c')

        try:
            feedbacks_dict = db['Feedbacks']
        except:
            print("Error in retrieving Feedbacks from feedback.db.")

        feedback = Feedback.Feedback(create_feedback_form.first_name.data, create_feedback_form.last_name.data, create_feedback_form.gender.data, create_feedback_form.membership.data, create_feedback_form.remarks.data, create_feedback_form.email.data)
        feedbacks_dict[feedback.get_feedback_id()] = feedback
        db['Feedbacks'] = feedbacks_dict

        db.close()

        return render_template('thankYou.html')
    return render_template('createFeedback.html', form=create_feedback_form)


@app.route('/retrieveFeedbacks')
def retrieve_feedbacks():
    feedbacks_dict = {}
    db = shelve.open('feedback.db', 'r')
    feedbacks_dict = db['Feedbacks']
    db.close()

    feedbacks_list = []
    for key in feedbacks_dict:
        feedback = feedbacks_dict.get(key)
        feedbacks_list.append(feedback)
    print(len(feedbacks_list))

    return render_template('retrieveFeedbacks.html', count=len(feedbacks_list), feedbacks_list=feedbacks_list)


@app.route('/updateFeedback/<int:id>/', methods=['GET', 'POST'])
def update_feedback(id):
    update_feedback_form = CreateFeedbackForm(request.form)
    if request.method == 'POST' and update_feedback_form.validate():
        feedbacks_dict = {}
        db = shelve.open('feedback.db', 'w')
        feedbacks_dict = db['Feedbacks']

        feedback = feedbacks_dict.get(id)
        feedback.set_first_name(update_feedback_form.first_name.data)
        feedback.set_last_name(update_feedback_form.last_name.data)
        feedback.set_gender(update_feedback_form.gender.data)
        feedback.set_membership(update_feedback_form.membership.data)
        feedback.set_remarks(update_feedback_form.remarks.data)
        feedback.set_email(update_feedback_form.email.data)

        db['Feedbacks'] = feedbacks_dict
        db.close()

        return redirect(url_for('retrieve_feedbacks'))
    else:
        feedbacks_dict = {}
        db = shelve.open('feedback.db', 'r')
        feedbacks_dict = db['Feedbacks']
        db.close()

        feedback = feedbacks_dict.get(id)
        update_feedback_form.first_name.data = feedback.get_first_name()
        update_feedback_form.last_name.data = feedback.get_last_name()
        update_feedback_form.gender.data = feedback.get_gender()
        update_feedback_form.membership.data = feedback.get_membership()
        update_feedback_form.remarks.data = feedback.get_remarks()
        update_feedback_form.email.data = feedback.get_email()
        update_feedback_form.email.data = feedback.get_email()

        return render_template('updateFeedback.html', form=update_feedback_form)


@app.route('/deleteFeedback/<int:id>', methods=['POST'])
def delete_feedback(id):
    feedbacks_dict = {}
    db = shelve.open('feedback.db', 'w')
    feedbacks_dict = db['Feedbacks']

    feedbacks_dict.pop(id)

    db['Feedbacks'] = feedbacks_dict
    db.close()

    return redirect(url_for('retrieve_feedbacks'))



if __name__ == '__main__':
    app.run()

