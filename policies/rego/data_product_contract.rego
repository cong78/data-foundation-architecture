package architecture.data_product_contract

import rego.v1

default allow := false

default applicable := false

live_product if input.lifecycle in {"go-live-approved", "active"}

applicable if live_product

contract := object.get(input, "contract", {})

violations contains {
	"criterionId": "DF-DATA-CRITERION-001",
	"message": "Live product does not reference a publishing contract id.",
} if {
	live_product
	object.get(contract, "id", "") == ""
}

violations contains {
	"criterionId": "DF-DATA-CRITERION-001",
	"message": "Publishing contract is not approved or published.",
} if {
	live_product
	status := object.get(contract, "status", "")
	status != "approved"
	status != "published"
}

violations contains {
	"criterionId": "DF-DATA-CRITERION-001",
	"message": "Publishing contract does not contain the product descriptor.",
} if {
	live_product
	object.get(contract, "productDescriptorEmbedded", false) != true
}

allow if {
	live_product
	count(violations) == 0
}

allow if not applicable

decision := {
	"policyId": "DF-DATA-RULE-001",
	"policyVersion": "1.0.0",
	"applicable": applicable,
	"allow": allow,
	"violations": [violation | some violation in violations],
}
