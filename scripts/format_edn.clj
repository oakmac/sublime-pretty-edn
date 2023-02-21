#!/usr/bin/env bb

(ns format-edn
  (:require
    [clojure.pprint :as pprint]
    [clojure.edn :as edn]))

(def input-txt (slurp *in*))
(def input-edn
  (try
    (edn/read-string input-txt)
    (catch Exception _err
      (throw (Exception. "Invalid EDN")))))

(pprint/pprint input-edn)
