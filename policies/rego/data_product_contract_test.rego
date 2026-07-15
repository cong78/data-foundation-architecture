package architecture.data_product_contract_test

import data.architecture.data_product_contract
import rego.v1

test_compliant_product_is_allowed if {
	result := data_product_contract.decision with input as {
		"productId": "customer-profile",
		"lifecycle": "active",
		"contract": {
			"id": "customer-profile-creation",
			"status": "published",
			"productDescriptorEmbedded": true,
		},
	}
	result.applicable
	result.allow
	count(result.violations) == 0
}

test_product_without_contract_is_denied if {
	result := data_product_contract.decision with input as {
		"productId": "customer-profile",
		"lifecycle": "go-live-approved",
	}
	not result.allow
	count(result.violations) == 3
}

test_incomplete_contract_is_denied if {
	result := data_product_contract.decision with input as {
		"productId": "customer-profile",
		"lifecycle": "active",
		"contract": {
			"id": "customer-profile-creation",
			"status": "draft",
			"productDescriptorEmbedded": false,
		},
	}
	result.applicable
	not result.allow
	count(result.violations) == 2
}

test_draft_product_is_out_of_scope if {
	result := data_product_contract.decision with input as {
		"productId": "customer-profile",
		"lifecycle": "draft",
	}
	not result.applicable
	result.allow
	count(result.violations) == 0
}
