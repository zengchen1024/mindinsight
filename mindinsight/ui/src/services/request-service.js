/**
 * Copyright 2019 Huawei Technologies Co., Ltd.All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import axios from './fetcher';

export default {
  // query dataset graph data
  queryDatasetGraph(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datasets/dataset_graph',
      params: params,
    });
  },

  // query dataset lineage
  getDatasetLineage() {
    return axios({
      method: 'post',
      url: 'v1/mindinsight/datasets/dataset_lineage',
    });
  },

  // query model versions
  queryModelVersions(params) {
    return axios({
      method: 'post',
      url: 'v1/mindinsight/models/model_lineage',
      data: params.body,
    });
  },

  // query summary list
  querySummaryList(params) {
    return axios({
      method: 'get',
      url: '/v1/mindinsight/datavisual/train-jobs',
      params: params,
    });
  },

  // query scalar sample
  getScalarsSample(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/scalar/metadata',
      params: params,
      headers: {
        ignoreError: true,
      },
    });
  },

  // query graph data
  queryGraphData(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/graphs/nodes',
      params: params,
    });
  },

  // search graph node
  searchNodesNames(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/graphs/nodes/names',
      params: params,
    });
  },

  // query the level of the node from the first layer based on node name
  querySingleNode(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/graphs/single-node',
      params: params,
    });
  },

  // query single train job list(image/scalar/graph)
  getSingleTrainJob(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/single-job',
      params: params,
    });
  },

  // query image meta data
  getImageMetadatas(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/image/metadata',
      params: params,
      headers: {
        ignoreError: true,
      },
    });
  },

  // query training job visualization plugins
  getDatavisualPlugins(params) {
    return axios({
      method: 'get',
      url: 'v1/mindinsight/datavisual/plugins',
      params: params,
    });
  },
};
