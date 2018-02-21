local utils = (import "jpy-utils.libsonnet");
{
  images: {
    release: {
      prombench: {
        creds: {
          host: "quay.io",
          password: "$QUAY_TOKEN",
          username: "prombench+gitlabci",
        },
        repo: "quay.io/ant31/prombench",
        tag: "${CI_COMMIT_REF_SLUG}-${SHA8}",
        name: utils.docker.containerName(self.repo, self.tag),
        get_name(tag):: utils.docker.containerName(self.repo, tag),
      },
    },
    ci: {
      prombench: {
        creds: {
          host: "quay.io",
          password: "$QUAY_TOKEN",
          username: "prombench+gitlabci",
        },
        repo: "quay.io/ant31/prombench",
        tag: "ci-${CI_COMMIT_REF_SLUG}-${SHA8}",
        name: utils.docker.containerName(self.repo, self.tag),
        get_name(tag):: utils.docker.containerName(self.repo, tag),
      },
    },
  },
}
