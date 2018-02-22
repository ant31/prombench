local kpm = import "kpm.libjsonnet";

function(
  params={}
)

kpm.package({
   package: {
      name: "ant31/promsnaps",
      expander: "jinja2",
      author: "Antoine Legrand",
      version: "0.0.1-1",
      description: "promsnaps",
      license: "Apache 2.0",
    },

    variables: {
      appname: "promsnaps",
      namespace: 'default',
      image: "quay.io/ant31/promsnaps:v0.0.1",
      svc_type: "LoadBalancer",
    },

    resources: [
      {
        file: "promsnaps-dp.yaml",
        template: (importstr "templates/promsnaps-dp.yaml"),
        name: "promsnaps",
        type: "deployment",
      },

      {
        file: "promsnaps-svc.yaml",
        template: (importstr "templates/promsnaps-svc.yaml"),
        name: "promsnaps",
        type: "service",
      }
      ],


    deploy: [
      {
        name: "$self",
      },
    ],


  }, params)
