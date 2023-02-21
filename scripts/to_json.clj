#!/usr/bin/env bb

(ns format-edn
  (:require
    [cheshire.core :as cheshire]
    [clojure.edn :as edn]
    [clojure.pprint :as pprint]
    [clojure.tools.cli :refer [parse-opts]]))

(def cli-args (:arguments (parse-opts *command-line-args* {})))

(def pretty? (not= "minified" (first cli-args)))

(def input-txt (slurp *in*))
(def input-edn
  (try
    (edn/read-string input-txt)
    (catch Exception _err
      (throw (Exception. "Invalid EDN")))))

(println (cheshire/generate-string input-edn {:pretty pretty?}))
