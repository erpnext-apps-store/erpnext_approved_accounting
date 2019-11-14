# -*- coding: utf-8 -*-
# Copyright (c) 2019, One Asset Management and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

from erpnext.accounts.doctype.payment_entry.payment_entry import PaymentEntry, InvalidPaymentEntry

class ApprovedPaymentEntry(PaymentEntry):
	def __init__(self, *args, **kwargs):
		super(ApprovedPaymentEntry, self).__init__(*args, **kwargs)

	def validate(self):
		super().validate()
