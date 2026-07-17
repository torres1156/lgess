name: Feature Request
description: Suggest a new feature or enhancement for the LG ESS Local integration.
title: "[Feature]: "
labels:
  - enhancement

body:
  - type: markdown
    attributes:
      value: |
        Thank you for helping improve LG ESS Local!

  - type: textarea
    id: problem
    attributes:
      label: Is your feature request related to a problem?
      description: Describe the problem or limitation you are experiencing.
      placeholder: "I'm always frustrated when..."
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: Describe the solution you'd like
      description: Explain the feature or improvement you would like to see.
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Describe alternatives you've considered
      description: Have you found another way to solve the problem?

  - type: textarea
    id: additional
    attributes:
      label: Additional information
      description: Add any screenshots, logs or other information that may help explain your request.
