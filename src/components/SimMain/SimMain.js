import { useState } from 'react';

// Styles
import './simMain.css';

// Components
import SimInfo from '../SimInfo/SimInfo';
import FaceTemplates from '../FaceTemplates/FaceTemplates';
import Attributes from '../Attributes/Attributes';
import Modifiers from '../Modifiers/Modifiers';

const SimMain = () => {
	const [gender, setGender] = useState(null);
	const [generateSim, setgenerateSim] = useState(false);

	const generateSimBtn = (e) => {
		e.preventDefault();
		if (!gender) return;
		setgenerateSim(!generateSim);
	};

	const content = (
		<div className='group'>
			<div className='group-1'>
				<SimInfo gender={gender} generateSim={generateSim} />
				<Attributes gender={gender} generateSim={generateSim} />
			</div>
			<div className='group-2'>
				<Modifiers />
			</div>
			<div className='group-3'>
				<FaceTemplates gender={gender} />
			</div>
		</div>
	);

	return (
		<>
			{/* Sim Gender Selector */}
			<section id='sim__gender'>
				<div className='sim__gender--select'>
					<h2>Choose a gender for created Sim</h2>
					<form>
						<div className='gender__selection'>
							<div>
								<input
									type='radio'
									name='gender'
									id='male'
									value='male'
									onChange={(e) => setGender(e.target.value)}
								/>
								<label htmlFor='male'>Male</label>
							</div>
							<div>
								<input
									type='radio'
									name='gender'
									id='female'
									value='female'
									onChange={(e) => setGender(e.target.value)}
								/>
								<label htmlFor='female'>Female</label>
							</div>
						</div>
						<button onClick={generateSimBtn}>Generate Sim</button>
					</form>
				</div>
			</section>

			{generateSim && content}

			<button onClick={generateSimBtn}>Reset</button>
		</>
	);
};
export default SimMain;
