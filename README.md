# cli-soql-query
Simple, low-overhead Python script to write SOQL queries at the command-line.

# Why?

Sometimes you just need a very small script to help you do some SOQL queries without anything too fancy. Configure your credentials using the YAML template provided to store multiple environments, then choose the environment at the command-line followed by a quote-escaped SOQL query. Results are returned to you in the shell, but can be piped to an external file and run through a JSON viewer.

(Currently, it only supports one live environment and defaults the rest of the config to Salesforce's sandbox URL.)
