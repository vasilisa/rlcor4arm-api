"""users routes"""
from flask import current_app as app, jsonify, request

from models import GameBlocks, BaseObject
from collections import OrderedDict
import numpy
import json


@app.route('/game_blocks/<game_id>/<block_id>', methods=["GET"])
def get_game_block(game_id,block_id): 
    
    query = GameBlocks.query.filter(GameBlocks.game_id==game_id, GameBlocks.block_number==block_id)
    if query != None:
        print('Exists')
        
    block  = query.first_or_404()

    # format the query into a dictionnary first:
    print(game_id)
    print(block_id)
    
    result                   = {}
    # arr_block                = numpy.array(participants.get_block_number()[0].replace('  ',' ').split(' '))
    # result['block_number']   = {i : arr_block[i] for i in range(0, len(arr_block))}
    arr_block                = block.get_block_number()[0].replace('  ',' ').split(' ')
    result['block_number']   = arr_block[0]

    # arr_block_type           = numpy.array(participants.get_block_type()[0:].replace('  ',' ').split(' '))
    # result['block_type']     = {0: arr_block_type[0]}
    arr_block_type           = block.get_block_type()[0:].replace('  ',' ').split(' ')
    result['block_type']     = arr_block_type[0]

    # arr_block_feedback       = numpy.array(participants.get_block_feedback()[0].replace('  ',' ').split(' '))
    # result['block_feedback'] = {0: arr_block_feedback[0]}

    arr_block_feedback       = block.get_block_feedback()[0].replace('  ',' ').split(' ')
    result['block_feedback'] = arr_block_feedback[0]
    
    
    arr_reward_1             = numpy.array(block.get_reward_1()[1:-1].replace('  ',' ').split(' '))
    result['reward_1']       = {i : arr_reward_1[i] for i in range(0, len(arr_reward_1))}

    arr_reward_2             = numpy.array(block.get_reward_2()[1:-1].replace('  ',' ').split(' '))
    result['reward_2']       = {i : arr_reward_2[i] for i in range(0, len(arr_reward_2))}

    arr_reward_3             = numpy.array(block.get_reward_3()[1:-1].replace('  ',' ').split(' '))
    result['reward_3']       = {i : arr_reward_3[i] for i in range(0, len(arr_reward_3))}

    arr_reward_4             = numpy.array(block.get_reward_4()[1:-1].replace('  ',' ').split(' '))
    result['reward_4']       = {i : arr_reward_4[i] for i in range(0, len(arr_reward_4))}


    arr_reward_1_th          = numpy.array(block.get_reward_1_th()[1:-1].replace('  ',' ').split(' '))
    result['th_reward_1']    = {i : arr_reward_1_th[i] for i in range(0, len(arr_reward_1_th))}

    arr_reward_2_th          = numpy.array(block.get_reward_2_th()[1:-1].replace('  ',' ').split(' '))
    result['th_reward_2']    = {i : arr_reward_2_th[i] for i in range(0, len(arr_reward_2_th))}

    arr_reward_3_th          = numpy.array(block.get_reward_3_th()[1:-1].replace('  ',' ').split(' '))
    result['th_reward_3']    = {i : arr_reward_3_th[i] for i in range(0, len(arr_reward_3_th))}

    arr_reward_4_th          = numpy.array(block.get_reward_4_th()[1:-1].replace('  ',' ').split(' '))
    result['th_reward_4']    = {i : arr_reward_4_th[i] for i in range(0, len(arr_reward_4_th))}


    arr_reward_upleft          = numpy.array(block.get_reward_upleft()[1:-1].replace('  ',' ').split(' '))
    result['reward_upleft']    = {i : arr_reward_upleft[i] for i in range(0, len(arr_reward_upleft))}

    arr_reward_upright         = numpy.array(block.get_reward_upright()[1:-1].replace('  ',' ').split(' '))
    result['reward_upright']   = {i : arr_reward_upright[i] for i in range(0, len(arr_reward_upright))}

    arr_reward_lowleft          = numpy.array(block.get_reward_lowleft()[1:-1].replace('  ',' ').split(' '))
    result['reward_lowleft']    = {i : arr_reward_lowleft[i] for i in range(0, len(arr_reward_lowleft))}

    arr_reward_lowright         = numpy.array(block.get_reward_lowright()[1:-1].replace('  ',' ').split(' '))
    result['reward_lowright']   = {i : arr_reward_lowright[i] for i in range(0, len(arr_reward_lowright))}


    arr_position1             = numpy.array(block.get_position1()[1:-1].replace('  ',' ').split(' '))
    result['position1']       = {i : arr_position1[i] for i in range(0, len(arr_position1))}

    arr_position2             = numpy.array(block.get_position2()[1:-1].replace('  ',' ').split(' '))
    result['position2']       = {i : arr_position2[i] for i in range(0, len(arr_position2))}

    arr_position3             = numpy.array(block.get_position3()[1:-1].replace('  ',' ').split(' '))
    result['position3']       = {i : arr_position3[i] for i in range(0, len(arr_position3))}

    arr_position4             = numpy.array(block.get_position4()[1:-1].replace('  ',' ').split(' '))
    result['position4']       = {i : arr_position4[i] for i in range(0, len(arr_position4))}


    app.logger.info(result)
    return jsonify(result), 200 # json.dumps(result)

