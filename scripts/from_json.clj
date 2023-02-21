#!/usr/bin/env bb

(ns format-edn
  (:require
    [cheshire.core :as cheshire]
    [clojure.edn :as edn]
    [clojure.pprint :as pprint]
    [clojure.tools.cli :refer [parse-opts]]))

(def cli-args (:arguments (parse-opts *command-line-args* {})))

(def keywordize? (= "keywordize" (first cli-args)))

(def input-txt (slurp *in*))
(def input-json
  (try
    (cheshire/parse-string-strict input-txt keywordize?)
    (catch Exception _err
      (throw (Exception. "Invalid JSON")))))

(pprint/pprint input-json)
