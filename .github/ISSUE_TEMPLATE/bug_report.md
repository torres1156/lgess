name: Bug Report
description: Report a problem with the LG ESS Local integration.
title: "[Bug]: "
labels:
  - bug

body:
  - type: markdown
    attributes:
      value: |
        Thank you for reporting a bug.

  - type: input
    id: ha_version
    attributes:
      label: Home Assistant Version
      placeholder: "2026.7.0"
    validations:
      required: true

  - type: input
    id: integration_version
    attributes:
      label: LG ESS Local Version
      placeholder: "0.2.0"
    validations:
      required: true

  - type: input
    id: firmware
    attributes:
      label: LG ESS Firmware
      placeholder: "Example: 5.14"

  - type: textarea
    id: description
    attributes:
      label: What happened?
      description: Describe the problem.
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: What did you expect?

  - type: textarea
    id: logs
    attributes:
      label: Relevant Logs
      render: text

  - type: textarea
    id: additional
    attributes:
      label: Additional Information
