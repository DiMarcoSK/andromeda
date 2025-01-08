package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"andromeda/internal/pipeline"

	"gopkg.in/yaml.v3"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("Usage: %s <path-to-yaml-file>", os.Args[0])
	}

	yamlFile := os.Args[1]
	fileContent, err := ioutil.ReadFile(yamlFile)
	if err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	var yamlData map[string]interface{}
	if err := yaml.Unmarshal(fileContent, &yamlData); err != nil {
		log.Fatalf("Invalid YAML syntax: %v", err)
	}

	pipelineType, err := pipeline.DetectPipelineType(yamlData)
	if err != nil {
		log.Fatalf("Error detecting pipeline type: %v", err)
	}

	switch pipelineType {
	case "gitlab":
		fmt.Println("GitLab pipeline check successful")
	case "github":
		fmt.Println("GitHub pipeline check successful")
	default:
		log.Fatalf("Unknown pipeline type")
	}
}
