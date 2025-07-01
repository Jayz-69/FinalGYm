# Copyright (c) 2025, Jayz and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class GymTrainerSubscription(Document):

    def on_submit(self):
        self.update_trainer_rating()

    def on_cancel(self):
        self.update_trainer_rating()

    def update_trainer_rating(self):
        if self.trainer:
            # Get all ratings of this trainer from active or completed subscriptions
            ratings = frappe.get_all('Gym Trainer Subscription',
                                     filters={'trainer': self.trainer, 'status': ['in', ['Active', 'Completed']], 'rating': ['!=', None]},
                                     fields=['rating'])
            if ratings:
                avg_rating = sum([r.rating for r in ratings]) / len(ratings)
            else:
                avg_rating = 0.0

            # Update average_rating in Gym Trainer
            frappe.db.set_value('Gym Trainer', self.trainer, 'average_rating', avg_rating)
            frappe.db.commit()

